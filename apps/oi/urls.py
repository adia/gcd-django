# -*- coding: utf-8 -*-
from django.core import urlresolvers
from django.conf.urls import patterns, url
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.generic import base as bv

from apps.oi import views as oi_views
from apps.oi import covers as oi_covers
from apps.oi import import_export as oi_import
from apps.oi import coordinators as oi_coordinators
from apps.oi import states

urlpatterns = patterns('',
    # General-purpose new record add page.
    url(r'^add/$',
        login_required(
          bv.TemplateView.as_view(template_name='oi/edit/add.html')),
        name='add'),

    url(r'^mentoring/$', oi_views.mentoring,
        name='mentoring'),

    # Creator URLs
    url(r'^creator/add/$',
     'apps.oi.views.add_creator', name='add_creator'),
    url(r'^creator/(?P<creator_id>\d+)/award/add/$',
     'apps.oi.views.add_creator_award', name='add_creator_award'),
    url(r'^creator/(?P<creator_id>\d+)/influence/add/$',
     'apps.oi.views.add_creator_artinfluence', name='add_creator_artinfluence'),
    url(r'^creator/(?P<creator_id>\d+)/membership/add/$',
     'apps.oi.views.add_creator_membership', name='add_creator_membership'),
    url(r'^creator/(?P<creator_id>\d+)/non_comic_work/add/$',
     'apps.oi.views.add_creator_noncomicwork', name='add_creator_noncomicwork'),
    url(r'^creator/(?P<creator_id>\d+)/school/add/$',
     'apps.oi.views.add_creator_school', name='add_creator_school'),
    url(r'^creator/(?P<creator_id>\d+)/degree/add/$',
     'apps.oi.views.add_creator_degree', name='add_creator_degree'),

    # Publisher URLs
    url(r'^publisher/add/$',
        oi_views.add_publisher,
        name='add_publisher'),
    url(r'^indicia_publisher/add/parent/(?P<parent_id>\d+)/$',
        oi_views.add_indicia_publisher,
        name='add_indicia_publisher'),
    url(r'^brand_group/add/parent/(?P<parent_id>\d+)/$',
        oi_views.add_brand_group,
        name='add_brand_group'),
    url(r'^brand/add/publisher/(?P<publisher_id>\d+)/$',
        oi_views.add_brand,
        name='add_brand_via_publisher'),
    url(r'^brand/add/group/(?P<brand_group_id>\d+)/$',
        oi_views.add_brand,
        name='add_brand_via_group'),
    url(r'^brand_use/add/brand/(?P<brand_id>\d+)/$',
        oi_views.add_brand_use,
        name='add_brand_use'),
    url(r'^brand_use/add/brand/(?P<brand_id>\d+)/publisher/(?P<publisher_id>\d+)/$',
        oi_views.add_brand_use,
        name='add_brand_use'),

    # Series URLs
    url(r'^series/add/publisher/(?P<publisher_id>\d+)/$',
        oi_views.add_series,
        name='add_series'),
    url(r'^series/(?P<series_id>\d+)/reorder/$',
        oi_views.reorder_series,
        name='reorder_series'),
    url(r'^series/(?P<series_id>\d+)/reorder/key_date/$',
        oi_views.reorder_series_by_key_date,
        name='reorder_series_key_date'),
    url(r'^series/(?P<series_id>\d+)/reorder/issue_number/$',
        oi_views.reorder_series_by_issue_number,
        name='reorder_series_issue_number'),
    url(r'^series/(?P<series_id>\d+)/edit_bonds/$',
        oi_views.edit_series_bonds, name='edit_series_bonds'),
    url(r'^series/revision/(?P<series_revision_id>\d+)/move/(?P<publisher_id>\d+)/$',
        oi_views.move_series, name='move_series'),

    url(r'^series_bond/revision/(?P<id>\d+)/$',
        oi_views.edit_series_bond, name='edit_series_bond'),
    url(r'^series_bond/add/(?P<id>\d+)/$',
        oi_views.add_series_bond, name='add_series_bond'),

    # Issue URLs
    url(r'^series/(?P<series_id>\d+)/add_issue/$', oi_views.add_issue,
        name='add_issue'),
    url(r'^series/(?P<series_id>\d+)/add_issues/$', oi_views.add_issues,
        name='add_issues'),
    url(r'^series/(?P<series_id>\d+)/add_issues/(?P<method>\w+)/$',
        oi_views.add_issues,
        name='add_multiple_issues'),
    url(r'^issue/(?P<issue_id>\d+)/add_variant_issue/$', oi_views.add_variant_issue,
        name='add_variant_issue'),
    url(r'^issue/(?P<issue_id>\d+)/add_variant_issue/(?P<cover_id>\d+)/$',
        oi_views.add_variant_issue, {'edit_with_base': True},
        name='add_variant_issue'),
    url(r'^issue/(?P<issue_id>\d+)/edit_two_issues/$',
        oi_views.edit_two_issues,
        name='edit_two_issues'),
    url(r'^issue/(?P<issue_one_id>\d+)/edit_with/(?P<issue_two_id>\d+)/$',
        oi_views.reserve_two_issues,
        name='reserve_two_issues'),

    url(r'^issue/(?P<issue_id>\d+)/export_issue/$',
        oi_import.export_issue_to_file,
        name='export_issue'),
    url(r'^issue/(?P<issue_id>\d+)/export_issue_csv/$',
        oi_import.export_issue_to_file, {'use_csv': True},
        name='export_issue_csv'),
    url(r'^issue_revision/(?P<issue_id>\d+)/export_issue_revision/$',
        oi_import.export_issue_to_file,  {'revision': True},
        name='export_issue_revision'),
    url(r'^issue_revision/(?P<issue_id>\d+)/export_issue_revision_csv/$',
        oi_import.export_issue_to_file, {'use_csv': True, 'revision': True},
        name='export_issue_revision_csv'),

    url(r'^issue/(?P<issue_id>\d+)/import_issue/(?P<changeset_id>\d+)/$',
        oi_import.import_issue_from_file,
        name='import_issue'),
    url(r'^issue/revision/(?P<issue_revision_id>\d+)/add_variant_to_issue_revision/(?P<changeset_id>\d+)$',
        oi_views.add_variant_to_issue_revision,
        name='add_variant_to_issue_revision'),
    url(r'^issue/revision/(?P<issue_revision_id>\d+)/add_story/(?P<changeset_id>\d+)$',
        oi_views.add_story,
        name='add_story'),
    url(r'^issue/(?P<issue_id>\d+)/import_stories/(?P<changeset_id>\d+)/$',
        oi_import.import_sequences_from_file,
        name='import_stories'),
    url(r'^issue/(?P<issue_id>\d+)/reorder_stories/(?P<changeset_id>\d+)$',
        oi_views.reorder_stories,
        name='reorder_stories'),
    url(r'^issue/revision/(?P<issue_revision_id>\d+)/move/(?P<series_id>\d+)/$',
        oi_views.move_issue, name='move_issue'),

    url(r'^bulk_issue_edit/$',
        oi_views.edit_issues_in_bulk,
        name='edit_issues_in_bulk'),

    # Story URLs
    # can be changed to r'^(?P<model_name>\w+)/revision/(?P<id>\d+)/remove/
    # later if needed
    url(r'^story/revision/(?P<id>\d+)/remove/$',
        oi_views.remove_story_revision,
        name='remove_story_revision'),
    url(r'^story/revision/(?P<id>\d+)/delete/$',
        oi_views.toggle_delete_story_revision,
        name='toggle_delete_story_revision'),
    url(r'^story/revision/(?P<id>\d+)/move/$', oi_views.move_story_revision,
        name='move_story_revision'),

    # Image URLs
    url(r'^(?P<model_name>\w+)/(?P<id>\d+)/upload_image/(?P<image_type>\w+)/$',
        oi_covers.upload_image,
        name='upload_image'),
    url(r'^(?P<model_name>\w+)/(?P<id>\d+)/replace_image/(?P<image_id>\d+)/$',
        oi_covers.replace_image,
        name='replace_image'),
    url(r'^mark_image_revision/(?P<revision_id>.+)/$', oi_covers.mark_image,
      {'marked': True}, name='mark_image_revision'),
    url(r'^unmark_image_revision/(?P<revision_id>.+)/$', oi_covers.mark_image,
      {'marked': False}, name='unmark_image_revision'),
    url(r'^mark_image/(?P<image_id>.+)/$', oi_covers.mark_image,
      {'marked': True}, name='mark_cover'),
    url(r'^unmark_image/(?P<image_id>.+)/$', oi_covers.mark_image,
      {'marked': False}, name='unmark_cover'),

    # Cover URLs
    url(r'^edit_covers/(?P<issue_id>\d+)/$', oi_covers.edit_covers,
      name='edit_covers'),
    url(r'^upload_cover/(?P<issue_id>\d+)/$', oi_covers.upload_cover,
      name='upload_cover'),
    url(r'^upload_variant/(?P<issue_id>\d+)/$', oi_covers.upload_variant,
      name='upload_variant'),
    url(r'^flip_artwork_flag/(?P<revision_id>.+)/$',
      oi_covers.flip_artwork_flag, name='flip_artwork_flag'),
    url(r'^replace_cover/(?P<cover_id>\d+)/$', oi_covers.upload_cover,
      name='replace_cover'),
    url(r'^gatefold_cover/$',
      oi_covers.process_edited_gatefold_cover, name='gatefold_cover'),
    url(r'^uploaded_cover/(?P<revision_id>\d+)/$', oi_covers.uploaded_cover,
      name='upload_cover_complete'),
    url(r'^mark_cover_revision/(?P<revision_id>.+)/$', oi_covers.mark_cover,
      {'marked': True}, name='mark_cover_revision'),
    url(r'^unmark_cover_revision/(?P<revision_id>.+)/$', oi_covers.mark_cover,
      {'marked': False}, name='unmark_cover_revision'),
    url(r'^mark_cover/(?P<cover_id>.+)/$', oi_covers.mark_cover,
      {'marked': True}, name='mark_cover'),
    url(r'^unmark_cover/(?P<cover_id>.+)/$', oi_covers.mark_cover,
      {'marked': False}, name='unmark_cover'),
    url(r'^cover/changeset/(?P<id>\d+)/move/$', oi_views.move_cover,
      name='move_cover'),
    url(r'^cover/(?P<cover_id>\d+)/changeset/(?P<id>\d+)/move/$', oi_views.move_cover,
      name='move_cover'),
    url(r'^cover/(?P<cover_id>\d+)/changeset/(?P<id>\d+)/undo_move$',
      oi_views.undo_move_cover, name='undo_move_cover'),

    url(r'^ongoing/$', oi_views.ongoing),
    url(r'^ongoing/(?P<series_id>\d+)/delete/$', oi_views.delete_ongoing,
        name='delete_ongoing'),

    url(r'^issue/revision/(?P<id>\d+)/list_reprints/$',
      oi_views.list_issue_reprints, name='list_issue_reprints'),
    url(r'^reserve_reprint/(?P<reprint_id>\d+)/type/(?P<reprint_type>.+)/edit/(?P<changeset_id>\d+)/$',
      oi_views.reserve_reprint, name='reserve_reprint'),
    url(r'^reprint/revision/(?P<id>\d+)/side/(?P<which_side>.+)/$',
      oi_views.edit_reprint, name='edit_reprint'),
    url(r'^reprint/revision/(?P<id>\d+)/$',
      oi_views.edit_reprint, name='edit_reprint'),

    url(r'^story/revision/(?P<story_id>\d+)/add_reprint/(?P<changeset_id>\d+)/reprint_note/(?P<reprint_note>.+|)/$',
      oi_views.add_reprint, name='add_story_reprint'),
    url(r'^story/revision/(?P<story_id>\d+)/add_reprint/(?P<changeset_id>\d+)/$',
      oi_views.add_reprint, name='add_story_reprint'),
      
    url(r'^issue/revision/(?P<issue_id>\d+)/add_reprint/(?P<changeset_id>\d+)/reprint_note/(?P<reprint_note>.+)/$',
      oi_views.add_reprint, name='add_issue_reprint'),
    url(r'^issue/revision/(?P<issue_id>\d+)/add_reprint/(?P<changeset_id>\d+)/$',
      oi_views.add_reprint, name='add_issue_reprint'),
      
    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/storyrevision/(?P<story_revision_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/story/(?P<story_two_id>\d+)/$',
      oi_views.save_reprint, name='save_revision_story_reprint'),
    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/storyrevision/(?P<story_revision_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/issue/(?P<issue_two_id>\d+)/$',
      oi_views.save_reprint, name='save_revision_issue_reprint'),
      
    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/storyrevision/(?P<story_revision_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/story/(?P<story_two_id>\d+)/$',
      oi_views.save_reprint, name='save_revision_story_reprint'),
    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/storyrevision/(?P<story_revision_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/issue/(?P<issue_two_id>\d+)/$',
      oi_views.save_reprint, name='save_revision_issue_reprint'),
      
    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/story/(?P<story_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/story/(?P<story_two_id>\d+)/$',
      oi_views.save_reprint, name='save_story_story_reprint'),
    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/story/(?P<story_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/issue/(?P<issue_two_id>\d+)/$',
      oi_views.save_reprint, name='save_story_issue_reprint'),

    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/issue/(?P<issue_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/story/(?P<story_two_id>\d+)/$',
      oi_views.save_reprint, name='save_issue_story_reprint'),
    url(r'^reprint/revision/(?P<reprint_revision_id>\d+)/issue/(?P<issue_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/issue/(?P<issue_two_id>\d+)/$',
      oi_views.save_reprint, name='save_issue_issue_reprint'),

    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/issue/(?P<issue_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/story/(?P<story_two_id>\d+)/$',
      oi_views.save_reprint, name='save_issue_story_reprint'),
    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/issue/(?P<issue_one_id>\d+)/confirm_reprint/(?P<changeset_id>\d+)/issue/(?P<issue_two_id>\d+)/$',
      oi_views.save_reprint, name='save_issue_issue_reprint'),

    url(r'^reprint/revision/(?P<id>\d+)/remove/$',
        oi_views.remove_reprint_revision, name='remove_reprint_revision'),
    url(r'^reprint/revision/(?P<id>\d+)/select_internal/issue/(?P<issue_id>\d+)/changeset/(?P<changeset_id>\d+)/side/(?P<which_side>.+)/$',
      oi_views.select_internal_object, name='select_internal_issue'),
    url(r'^reprint/revision/(?P<id>\d+)/select_internal/story/(?P<story_id>\d+)/changeset/(?P<changeset_id>\d+)/side/(?P<which_side>.+)/$',
      oi_views.select_internal_object, name='select_internal_story'),

    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/create_sequence/issue/(?P<issue_id>\d+)/story/(?P<story_id>\d+)/$',
      oi_views.create_matching_sequence, name='create_matching_sequence'),
    url(r'^reprint/revision/(?P<reprint_revision_id>.+)/create_edit_sequence/issue/(?P<issue_id>\d+)/story/(?P<story_id>\d+)/$',
      oi_views.create_matching_sequence, {'edit' : 'True'}, name='create_edit_matching_sequence'),

    # Generic URLs
    url(r'^(?P<model_name>\w+)/(?P<id>\d+)/reserve/$', oi_views.reserve,
        name='reserve_revision'),
    url(r'^(?P<model_name>\w+)/(?P<id>\d+)/delete/$', oi_views.delete,
        name='delete_revision'),
    url(r'^(?P<model_name>\w+)/revision/(?P<id>\d+)/edit/$',
        oi_views.edit_revision,
        name='edit_revision'),
    url(r'^changeset/(?P<id>\d+)/edit/$', oi_views.edit, name='edit'),
    url(r'^changeset/(?P<id>\d+)/submit/$', oi_views.submit, name='submit'),
    url(r'^changeset/(?P<id>\d+)/retract/$', oi_views.retract, name='retract'),
    url(r'^changeset/(?P<id>\d+)/discard/$', oi_views.discard, name='discard'),
    url(r'^changeset/(?P<id>\d+)/(?P<has_comment>\d+)/confirm_discard/$', oi_views.confirm_discard,
        name='confirm_discard'),
    url(r'^changeset/(?P<id>\d+)/assign/$', oi_views.assign, name='assign'),
    url(r'^changeset/(?P<id>\d+)/release/$', oi_views.release, name='release'),
    url(r'^changeset/(?P<id>\d+)/approve/$', oi_views.approve, name='approve'),
    url(r'^changeset/(?P<id>\d+)/disapprove/$', oi_views.disapprove,
        name='disapprove'),
    url(r'^changeset/(?P<id>\d+)/process/$', oi_views.process, name='process'),
    url(r'^(?P<model_name>\w+)/revision/(?P<id>\d+)/process/$',
        oi_views.process_revision,
        name='process_revision'),
    url(r'^changeset/(?P<id>\d+)/compare/$', oi_views.compare, name='compare'),
    url(r'^(?P<model_name>\w+)/revision/(?P<id>\d+)/preview/$', oi_views.preview,
        name='preview_revision'),

    # queue URLs
    url(r'^queues/editing/$', oi_views.show_queue,
       {'queue_name': 'editing', 'state': states.OPEN },
        name='editing'),
    url(r'^queues/pending/$', oi_views.show_queue,
       {'queue_name': 'pending', 'state': states.PENDING },
        name='pending'),
    url(r'^queues/reviews/$', oi_views.show_queue,
       {'queue_name': 'reviews', 'state': states.REVIEWING },
        name='reviewing'),
    url(r'^queues/editor_log/$', oi_views.show_queue,
       {'queue_name': 'editor_log', 'state': states.APPROVED },
        name='editor_log'),
    url(r'^queues/approved/$', oi_views.show_queue,
       {'queue_name': 'approved', 'state': states.APPROVED },
        name='approved'),
    url(r'^queues/covers_pending/$', oi_views.show_queue,
       {'queue_name': 'covers', 'state': states.PENDING },
        name='pending_covers'),

    url(r'^coordinator/clear_publisher_series',
      oi_coordinators.clear_reservations_one_week,
      {}, name='clear_publisher_series'),
    url(r'^coordinator/clear_issues',
      oi_coordinators.clear_reservations_three_weeks,
      {}, name='clear_issues'),
    url(r'^coordinator/$',
        bv.TemplateView.as_view(template_name='oi/edit/coordinators.html'),
        name='coordinators_toc'),
)

urlpatterns += patterns('',
    (r'^changeset/(?P<id>\d+)/$', bv.RedirectView.as_view(url='compare',
                                                          permanent=False)),
)
